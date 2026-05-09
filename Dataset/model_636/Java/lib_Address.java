





import java.util.List;
import java.util.ArrayList;

public class lib_Address  {

    private String postalCode;





    private lib_Library lib_library;


    public lib_Address(
        String postalCode    ) {
        this.postalCode = postalCode;
    }


    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }

    public lib_Library getLib_library() {
        return lib_library;
    }

    public void setLib_library(lib_Library lib_library) {
        this.lib_library = lib_library;
    }

}