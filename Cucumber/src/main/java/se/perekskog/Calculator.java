package se.perekskog;

public class Calculator
{
    public Calculator()
    {
        state = 0;
        System.out.println("===calc=== init calculator");
    }

    public void add(int i)
    {
        state = state + i;
        System.out.println("===calc=== add " + i);
    }

    public int state()
    {
        System.out.println("===calc=== return state = " + state);
        return state;
    }

    private int state;
}