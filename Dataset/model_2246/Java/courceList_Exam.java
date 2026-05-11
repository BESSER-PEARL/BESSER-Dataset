




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class courceList_Exam  {

    private int lenght;
    private int weight;
    private String form;
    private LocalDate date;



    public courceList_Exam(
        int lenght,        int weight,        String form,        LocalDate date    ) {
        this.lenght = lenght;
        this.weight = weight;
        this.form = form;
        this.date = date;
    }


    public int getLenght() {
        return lenght;
    }

    public void setLenght(int lenght) {
        this.lenght = lenght;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}