





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookings_BookingsManager extends IBookings {






    private IBills ibills;




    private IStays istays;




    private CustomerProvides customerprovides;




    private IBookablesAccess ibookablesaccess;




    private IGuests iguests;




    private ICustomers icustomers;


    public Classes_Bookings_BookingsManager(
    ) {
        super(
        );
    }



    public IBills getIbills() {
        return ibills;
    }

    public void setIbills(IBills ibills) {
        this.ibills = ibills;
    }
    public IStays getIstays() {
        return istays;
    }

    public void setIstays(IStays istays) {
        this.istays = istays;
    }
    public CustomerProvides getCustomerprovides() {
        return customerprovides;
    }

    public void setCustomerprovides(CustomerProvides customerprovides) {
        this.customerprovides = customerprovides;
    }
    public IBookablesAccess getIbookablesaccess() {
        return ibookablesaccess;
    }

    public void setIbookablesaccess(IBookablesAccess ibookablesaccess) {
        this.ibookablesaccess = ibookablesaccess;
    }
    public IGuests getIguests() {
        return iguests;
    }

    public void setIguests(IGuests iguests) {
        this.iguests = iguests;
    }
    public ICustomers getIcustomers() {
        return icustomers;
    }

    public void setIcustomers(ICustomers icustomers) {
        this.icustomers = icustomers;
    }

}