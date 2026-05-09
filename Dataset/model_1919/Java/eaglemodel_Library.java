





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Library  {

    private String name;





    private eaglemodel_Libraries eaglemodel_libraries;




    private eaglemodel_Symbols eaglemodel_symbols;




    private eaglemodel_Description eaglemodel_description;




    private eaglemodel_Devicesets eaglemodel_devicesets;


    public eaglemodel_Library(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eaglemodel_Libraries getEaglemodel_libraries() {
        return eaglemodel_libraries;
    }

    public void setEaglemodel_libraries(eaglemodel_Libraries eaglemodel_libraries) {
        this.eaglemodel_libraries = eaglemodel_libraries;
    }
    public eaglemodel_Symbols getEaglemodel_symbols() {
        return eaglemodel_symbols;
    }

    public void setEaglemodel_symbols(eaglemodel_Symbols eaglemodel_symbols) {
        this.eaglemodel_symbols = eaglemodel_symbols;
    }
    public eaglemodel_Description getEaglemodel_description() {
        return eaglemodel_description;
    }

    public void setEaglemodel_description(eaglemodel_Description eaglemodel_description) {
        this.eaglemodel_description = eaglemodel_description;
    }
    public eaglemodel_Devicesets getEaglemodel_devicesets() {
        return eaglemodel_devicesets;
    }

    public void setEaglemodel_devicesets(eaglemodel_Devicesets eaglemodel_devicesets) {
        this.eaglemodel_devicesets = eaglemodel_devicesets;
    }

}