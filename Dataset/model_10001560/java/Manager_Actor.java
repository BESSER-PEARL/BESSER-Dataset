





import java.util.List;
import java.util.ArrayList;

public class Manager_Actor  {






    private statistical_reporting_UseCase statistical_reporting_usecase;




    private vehicle_management_UseCase vehicle_management_usecase;




    private account_management_UseCase account_management_usecase;




    private customer_management_UseCase customer_management_usecase;


    public Manager_Actor(
    ) {
    }



    public statistical_reporting_UseCase getStatistical_reporting_usecase() {
        return statistical_reporting_usecase;
    }

    public void setStatistical_reporting_usecase(statistical_reporting_UseCase statistical_reporting_usecase) {
        this.statistical_reporting_usecase = statistical_reporting_usecase;
    }
    public vehicle_management_UseCase getVehicle_management_usecase() {
        return vehicle_management_usecase;
    }

    public void setVehicle_management_usecase(vehicle_management_UseCase vehicle_management_usecase) {
        this.vehicle_management_usecase = vehicle_management_usecase;
    }
    public account_management_UseCase getAccount_management_usecase() {
        return account_management_usecase;
    }

    public void setAccount_management_usecase(account_management_UseCase account_management_usecase) {
        this.account_management_usecase = account_management_usecase;
    }
    public customer_management_UseCase getCustomer_management_usecase() {
        return customer_management_usecase;
    }

    public void setCustomer_management_usecase(customer_management_UseCase customer_management_usecase) {
        this.customer_management_usecase = customer_management_usecase;
    }

}