#include <iostream>
class subvector
{
public:
    subvector()
    {
        this->capacity = 0;
        this->top = 0;
        this->mas = NULL;
    }

    ~subvector()
    {
        delete[] this->mas;
    }

    void resize(unsigned int new_capacity)
    {
        int* n = new int[new_capacity];

        for (unsigned int i = 0; i < this->top; i++)
        {
            n[i] = this->mas[i];
        }

        delete[] this->mas;
        this->mas = n;
        this->capacity = new_capacity;
    }

    void push_back(int d)
    {
        if (this->top == this->capacity)
        {
            resize(2 * this->capacity + 1);
        }
        this->mas[this->top] = d;
        this->top++;
    }

    int pop_back()
    {
        if (this->top == 0)
            return 0;
        else
        {
            this->top--;
            return this->mas[this->top];
        }
    }

    void shrink_to_fit()
    {
        if (this->capacity > this->top)
        {
            int* n = new int[this->top];
            int size = this->top;

            for (unsigned int i = 0; i < this->top; i++)
            {
                n[i] = this->mas[i];
            }
            delete[] this->mas;
            this->mas = n;
            this->top = size;
            this->capacity = size;
        }
    }

    void clear()
    {
        this->top = 0;
    }

    unsigned int size()
    {
        //return this->top + 1;
        return this->capacity + 1;
    }
private:
    int* mas;
    unsigned int top;
    unsigned int capacity;
};

int main()
{
    subvector sv;
    sv.resize(20);
    for (int i = 1; i < 11; i++)
    {
        sv.push_back(i);
    }
    sv.shrink_to_fit();
    unsigned int d = sv.size();
    for (int i = 1; i < d; i++)
    {
        std::cout << sv.pop_back() << std::endl;
    }
    return 0;
}
