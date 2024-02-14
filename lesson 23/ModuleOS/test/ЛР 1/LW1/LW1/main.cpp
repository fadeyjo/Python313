#include "glew.h"
#include "glut.h"

GLfloat windowWidth = 1500;
GLfloat windowHeight = 800;

GLfloat rSize = 25;
GLfloat xStart = -(rSize * 0.5);
GLfloat yStart = 99;

int startStepTime = 20;

float startStep = 0.3;

void RenderScene(void) {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0f, 0.0f, 0.0f);
	glRectf(xStart, yStart, xStart + rSize, yStart - rSize);
	glutSwapBuffers();
}

void TimerFunction(int value) {
	yStart -= startStep;
	if (yStart >= -75) {
		startStep += 0.3;
		glutPostRedisplay();
		glutTimerFunc(startStepTime, TimerFunction, 1);
	}
	else {
		yStart = -75;
		glutPostRedisplay();
		glutTimerFunc(startStepTime, TimerFunction, 1);
	}
}

void SetupRC(void) {
	glClearColor(0.0f, 0.0f, 1.0f, 1.0f);
}

void ChangeSize(GLsizei w, GLsizei h) {
	GLfloat aspectRatio;
	if (h == 0) {
		h = 1;
	}
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	aspectRatio = (GLfloat)w / (GLfloat)h;
	if (w <= h)
	{
		windowWidth = 100;
		windowHeight = 100 / aspectRatio;
		glOrtho(-100.0, 100.0, -windowHeight, windowHeight, 1.0, -1.0);
	}
	else
	{
		windowWidth = 100 * aspectRatio; windowHeight = 100;
		glOrtho(-windowWidth, windowWidth, -100.0, 100.0, 1.0, -1.0);
	}
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void main() {
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB); 
	glutInitWindowSize(windowWidth, windowHeight);
	glutCreateWindow("Falling Square");
	glutDisplayFunc(RenderScene);
	glutReshapeFunc(ChangeSize);
	glutTimerFunc(startStepTime, TimerFunction, 1);
	SetupRC();
	glutMainLoop();
}