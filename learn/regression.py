# coding: utf8

import numpy as np
from pylab import *
from sklearn import linear_model


# Для вопроизодимости результатов, зависящих от генератора случайных чисел
np.random.seed(1000)


# Настройка шрифтов для будущих графиков
rcParams['font.family'] = 'DejaVu Sans' # Понимает русские буквы
rcParams['font.size'] = 16


# ---------------- Создание модельных данных  -----------------------
mean1 = [0.5, 2]

cov1 = [[1, 1.1], [-1.1, 1]]

mean2 = [2.3, -0.5]
cov2 = [[1.3, -1.5], [1.5, 1.6]]


# Данные первого класса
data1 = np.random.multivariate_normal(mean1, cov1, 100)
# Данные второго класса
data2 = np.random.multivariate_normal(mean2, cov2, 100)

# -------------------------------------------------------------------

# Формируем обучающую выборку
X = np.vstack([data1, data2])
# Групповая переменная
Y = [0]*len(data1) + [1]*len(data2)


# Настраиваем модель логистической регрессии
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)


# Массив точек для классификации и последующей заливки в соотвтетсвии с классом
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# Выполнение классификации каждой точки массива
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# логарифмы вероятностей принадлежности к классам
probabilities = logreg.predict_log_proba(np.c_[xx.ravel(), yy.ravel()])


# преобразование формата (как требует pcolormesh)
Z = Z.reshape(xx.shape)
p1 = probabilities[:,0].reshape(xx.shape)
p2 = probabilities[:,1].reshape(xx.shape)

# -------------------------------------------------------------------

# Отрисовка результатов классификации и оценок вероятностей

title(u'Результаты классификации')
plot(data1[:, 0], data1[:, 1], 'oy')
plot(data2[:, 0], data2[:, 1], 'sc')
pcolormesh(xx, yy, Z, cmap='RdYlBu')
gca().set_xlim([x_min, x_max])
gca().set_ylim([y_min, y_max])


figure()
title(u'Лог-Вероятности класса 1')
pcolormesh(xx, yy, p1, cmap='cool')
colorbar()
gca().set_xlim([x_min, x_max])
gca().set_ylim([y_min, y_max])


figure()
title(u'Лог-Вероятности класса 2')
pcolormesh(xx, yy, p2, cmap='cool')
colorbar()
gca().set_xlim([x_min, x_max])
gca().set_ylim([y_min, y_max])


show()