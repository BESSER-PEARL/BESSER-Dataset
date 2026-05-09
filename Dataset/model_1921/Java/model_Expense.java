




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Expense  {

    private float price;
    private int receiptId;
    private boolean fixed;
    private int id;
    private LocalDate date;
    private String name;
    private String description;





    private model_Room model_room;


    public model_Expense(
        float price,        int receiptId,        boolean fixed,        int id,        LocalDate date,        String name,        String description    ) {
        this.price = price;
        this.receiptId = receiptId;
        this.fixed = fixed;
        this.id = id;
        this.date = date;
        this.name = name;
        this.description = description;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getReceiptid() {
        return receiptId;
    }

    public void setReceiptid(int receiptId) {
        this.receiptId = receiptId;
    }
    public boolean getFixed() {
        return fixed;
    }

    public void setFixed(boolean fixed) {
        this.fixed = fixed;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public model_Room getModel_room() {
        return model_room;
    }

    public void setModel_room(model_Room model_room) {
        this.model_room = model_room;
    }

}