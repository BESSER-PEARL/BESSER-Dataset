




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Receipt  {

    private LocalDate Date;
    private float totalCost;
    private int id;





    private List<model_Expense> model_expenses;




    private model_Room model_room;


    public model_Receipt(
        LocalDate Date,        float totalCost,        int id    ) {
        this.Date = Date;
        this.totalCost = totalCost;
        this.id = id;
        this.model_expenses = new ArrayList<>();
    }

    public model_Receipt(
        LocalDate Date,        float totalCost,        int id        ArrayList<model_Expense> model_expenses    ) {
        this.Date = Date;
        this.totalCost = totalCost;
        this.id = id;
        this.model_expenses = model_expenses;
    }

    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public float getTotalcost() {
        return totalCost;
    }

    public void setTotalcost(float totalCost) {
        this.totalCost = totalCost;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<model_Expense> getModel_expenses() {
        return model_expenses;
    }

    public void addModel_expense(Model_expense model_expense) {
        this.model_expenses.add(model_expense);
    }
    public model_Room getModel_room() {
        return model_room;
    }

    public void setModel_room(model_Room model_room) {
        this.model_room = model_room;
    }

}