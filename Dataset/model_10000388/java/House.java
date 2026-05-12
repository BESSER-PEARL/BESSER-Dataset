





import java.util.List;
import java.util.ArrayList;

public class House  {

    private int numberOfFloors;
    private int price;
    private int fees;
    private int sizeOfProperty;



    public House(
        int numberOfFloors,        int price,        int fees,        int sizeOfProperty    ) {
        this.numberOfFloors = numberOfFloors;
        this.price = price;
        this.fees = fees;
        this.sizeOfProperty = sizeOfProperty;
    }


    public int getNumberoffloors() {
        return numberOfFloors;
    }

    public void setNumberoffloors(int numberOfFloors) {
        this.numberOfFloors = numberOfFloors;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getFees() {
        return fees;
    }

    public void setFees(int fees) {
        this.fees = fees;
    }
    public int getSizeofproperty() {
        return sizeOfProperty;
    }

    public void setSizeofproperty(int sizeOfProperty) {
        this.sizeOfProperty = sizeOfProperty;
    }


}