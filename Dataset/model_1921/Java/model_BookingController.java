





import java.util.List;
import java.util.ArrayList;

public class model_BookingController extends CustomerInterface {






    private model_ExpenseExpert model_expenseexpert;




    private model_PromotionExpert model_promotionexpert;




    private model_RoomExpert model_roomexpert;




    private model_BookingExpert model_bookingexpert;




    private model_DatabaseInterface model_databaseinterface;


    public model_BookingController(
    ) {
        super(
        );
    }



    public model_ExpenseExpert getModel_expenseexpert() {
        return model_expenseexpert;
    }

    public void setModel_expenseexpert(model_ExpenseExpert model_expenseexpert) {
        this.model_expenseexpert = model_expenseexpert;
    }
    public model_PromotionExpert getModel_promotionexpert() {
        return model_promotionexpert;
    }

    public void setModel_promotionexpert(model_PromotionExpert model_promotionexpert) {
        this.model_promotionexpert = model_promotionexpert;
    }
    public model_RoomExpert getModel_roomexpert() {
        return model_roomexpert;
    }

    public void setModel_roomexpert(model_RoomExpert model_roomexpert) {
        this.model_roomexpert = model_roomexpert;
    }
    public model_BookingExpert getModel_bookingexpert() {
        return model_bookingexpert;
    }

    public void setModel_bookingexpert(model_BookingExpert model_bookingexpert) {
        this.model_bookingexpert = model_bookingexpert;
    }
    public model_DatabaseInterface getModel_databaseinterface() {
        return model_databaseinterface;
    }

    public void setModel_databaseinterface(model_DatabaseInterface model_databaseinterface) {
        this.model_databaseinterface = model_databaseinterface;
    }

}