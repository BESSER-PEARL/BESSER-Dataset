





import java.util.List;
import java.util.ArrayList;

public class APNRepository_Interface  {






    private APNProgrammaticModel apnprogrammaticmodel;




    private APNStore_Interface apnstore_interface;




    private APNCache_Interface apncache_interface;


    public APNRepository_Interface(
    ) {
    }



    public APNProgrammaticModel getApnprogrammaticmodel() {
        return apnprogrammaticmodel;
    }

    public void setApnprogrammaticmodel(APNProgrammaticModel apnprogrammaticmodel) {
        this.apnprogrammaticmodel = apnprogrammaticmodel;
    }
    public APNStore_Interface getApnstore_interface() {
        return apnstore_interface;
    }

    public void setApnstore_interface(APNStore_Interface apnstore_interface) {
        this.apnstore_interface = apnstore_interface;
    }
    public APNCache_Interface getApncache_interface() {
        return apncache_interface;
    }

    public void setApncache_interface(APNCache_Interface apncache_interface) {
        this.apncache_interface = apncache_interface;
    }

}