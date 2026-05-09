





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_StaffRole  {

    private boolean canManageAccounts;
    private String name;
    private boolean canManageRooms;
    private boolean canManageServices;
    private boolean canManageBookings;



    public CodePack_DataModels_StaffRole(
        boolean canManageAccounts,        String name,        boolean canManageRooms,        boolean canManageServices,        boolean canManageBookings    ) {
        this.canManageAccounts = canManageAccounts;
        this.name = name;
        this.canManageRooms = canManageRooms;
        this.canManageServices = canManageServices;
        this.canManageBookings = canManageBookings;
    }


    public boolean getCanmanageaccounts() {
        return canManageAccounts;
    }

    public void setCanmanageaccounts(boolean canManageAccounts) {
        this.canManageAccounts = canManageAccounts;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCanmanagerooms() {
        return canManageRooms;
    }

    public void setCanmanagerooms(boolean canManageRooms) {
        this.canManageRooms = canManageRooms;
    }
    public boolean getCanmanageservices() {
        return canManageServices;
    }

    public void setCanmanageservices(boolean canManageServices) {
        this.canManageServices = canManageServices;
    }
    public boolean getCanmanagebookings() {
        return canManageBookings;
    }

    public void setCanmanagebookings(boolean canManageBookings) {
        this.canManageBookings = canManageBookings;
    }


}