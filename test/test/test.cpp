#define _CRT_SECURE_NO_WARNINGS //strcpy �ذ�
#include <iostream>
using namespace std;

class Person{
private:
	char* m_name;
	int m_age;
public:
	Person();
	Person(const char* name, const int& age);
	Person(const Person& p);
	~Person();
	void setName(const char* name);
	void setAge(const int& age);
	Person& aging();
	void showInfo() const;
};

Person& Person::aging(){ //���۷��� Ÿ���̹Ƿ� ��Ÿ�� ���� ����
	this->m_age++;
	return *this;
}

Person::Person()
:m_age(0)
{
	cout << "����Ʈ ������" << endl;
	m_name = new char[strlen("�̸�����") + 1];
	strcpy(m_name, "�̸�����");
}

Person::Person(const char* name, const int& age)
:m_age(age)
{
	cout << "�����ִ� ������" << endl;
	m_name = new char[strlen(name) + 1];
	strcpy(m_name, name);
}

Person::Person(const Person& p)
	:m_age(p.m_age)
{
	cout << "���� ������" << endl;
	m_name = new char[strlen(p.m_name) + 1];
	strcpy(m_name, p.m_name);
}

Person::~Person(){
	cout << "�Ҹ���" << endl;
	delete[] m_name;
}

void Person::setName(const char* name){
	if (m_name != NULL)
		delete[] m_name; //�޸� ���� ����!
	m_name = new char[strlen(name) + 1];
	strcpy(m_name, name);
}

void Person::setAge(const int& age){
	m_age = age;
}


void Person::showInfo() const{
	cout << "�ּ� : " << this << endl;
	cout << "�̸� : " << m_name << endl;
	cout << "���� : " << m_age << endl;
}
int main(){
	cout << "201111265 �躴��" << endl;

	Person std1("ȫ�浿", 20);

	Person std2(std1);
	Person std3 = std1;
	std3.showInfo();

	std3.aging();
	//std2 = std3;
	return 0;
}

//Ȯ���ϰ� ����� �Ҵ�