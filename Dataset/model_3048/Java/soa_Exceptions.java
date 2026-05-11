





import java.util.List;
import java.util.ArrayList;

public class soa_Exceptions  {






    private soa_Module soa_module;




    private List<soa_Exception> soa_exceptions;


    public soa_Exceptions(
    ) {
        this.soa_exceptions = new ArrayList<>();
    }

    public soa_Exceptions(
        ArrayList<soa_Exception> soa_exceptions    ) {
        this.soa_exceptions = soa_exceptions;
    }


    public soa_Module getSoa_module() {
        return soa_module;
    }

    public void setSoa_module(soa_Module soa_module) {
        this.soa_module = soa_module;
    }
    public List<soa_Exception> getSoa_exceptions() {
        return soa_exceptions;
    }

    public void addSoa_exception(Soa_exception soa_exception) {
        this.soa_exceptions.add(soa_exception);
    }

}