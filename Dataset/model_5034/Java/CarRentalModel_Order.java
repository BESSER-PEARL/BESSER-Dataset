




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_Order  {

    private LocalDate orderDate;
    private float price;





    private CarRentalModel_Customer carrentalmodel_customer;




    private CarRentalModel_Craft carrentalmodel_craft;




    private CarRentalModel_Craft carrentalmodel_craft;




    private CarRentalModel_Customer carrentalmodel_customer;


    public CarRentalModel_Order(
        LocalDate orderDate,        float price    ) {
        this.orderDate = orderDate;
        this.price = price;
    }


    public LocalDate getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(LocalDate orderDate) {
        this.orderDate = orderDate;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public CarRentalModel_Customer getCarrentalmodel_customer() {
        return carrentalmodel_customer;
    }

    public void setCarrentalmodel_customer(CarRentalModel_Customer carrentalmodel_customer) {
        this.carrentalmodel_customer = carrentalmodel_customer;
    }
    public CarRentalModel_Craft getCarrentalmodel_craft() {
        return carrentalmodel_craft;
    }

    public void setCarrentalmodel_craft(CarRentalModel_Craft carrentalmodel_craft) {
        this.carrentalmodel_craft = carrentalmodel_craft;
    }
    public CarRentalModel_Craft getCarrentalmodel_craft() {
        return carrentalmodel_craft;
    }

    public void setCarrentalmodel_craft(CarRentalModel_Craft carrentalmodel_craft) {
        this.carrentalmodel_craft = carrentalmodel_craft;
    }
    public CarRentalModel_Customer getCarrentalmodel_customer() {
        return carrentalmodel_customer;
    }

    public void setCarrentalmodel_customer(CarRentalModel_Customer carrentalmodel_customer) {
        this.carrentalmodel_customer = carrentalmodel_customer;
    }

}