





import java.util.List;
import java.util.ArrayList;

public class Showroom  {

    private int Year;
    private String Model;
    private String Car_Make;
    private String Price_Range;
    private int Horsepower;





    private Customer customer;


    public Showroom(
        int Year,        String Model,        String Car_Make,        String Price_Range,        int Horsepower    ) {
        this.Year = Year;
        this.Model = Model;
        this.Car_Make = Car_Make;
        this.Price_Range = Price_Range;
        this.Horsepower = Horsepower;
    }


    public int getYear() {
        return Year;
    }

    public void setYear(int Year) {
        this.Year = Year;
    }
    public String getModel() {
        return Model;
    }

    public void setModel(String Model) {
        this.Model = Model;
    }
    public String getCar_make() {
        return Car_Make;
    }

    public void setCar_make(String Car_Make) {
        this.Car_Make = Car_Make;
    }
    public String getPrice_range() {
        return Price_Range;
    }

    public void setPrice_range(String Price_Range) {
        this.Price_Range = Price_Range;
    }
    public int getHorsepower() {
        return Horsepower;
    }

    public void setHorsepower(int Horsepower) {
        this.Horsepower = Horsepower;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}