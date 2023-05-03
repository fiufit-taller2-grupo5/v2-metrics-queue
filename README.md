# Metrics

Este proyecto almacena métricas que mandan otros microservicios, usando un protoclo sencillo.

Los distintos microservicios (producers) generan métricas para la aplicación, y cuando quieren registrarlas, envían una request HTTP de tipo POST a este servidor, quien almacena la métrica en una Base de Datos Redis (par clave-valor). Esto nos permite contar cuál es la cantidad de cada métrica.

El Body de las requests deben tener el siguiente formato:
