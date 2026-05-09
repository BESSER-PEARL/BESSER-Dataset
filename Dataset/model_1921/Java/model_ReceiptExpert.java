





import java.util.List;
import java.util.ArrayList;

public class model_ReceiptExpert  {






    private model_DatabaseInterface model_databaseinterface;




    private model_BookingController model_bookingcontroller;


    public model_ReceiptExpert(
    ) {
    }



    public model_DatabaseInterface getModel_databaseinterface() {
        return model_databaseinterface;
    }

    public void setModel_databaseinterface(model_DatabaseInterface model_databaseinterface) {
        this.model_databaseinterface = model_databaseinterface;
    }
    public model_BookingController getModel_bookingcontroller() {
        return model_bookingcontroller;
    }

    public void setModel_bookingcontroller(model_BookingController model_bookingcontroller) {
        this.model_bookingcontroller = model_bookingcontroller;
    }

}