





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Description  {

    private String language;
    private String value;





    private eaglemodel_Symbol eaglemodel_symbol;




    private eaglemodel_Sheet eaglemodel_sheet;




    private eaglemodel_Schematic eaglemodel_schematic;




    private eaglemodel_Deviceset eaglemodel_deviceset;




    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_Description(
        String language,        String value    ) {
        this.language = language;
        this.value = value;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eaglemodel_Symbol getEaglemodel_symbol() {
        return eaglemodel_symbol;
    }

    public void setEaglemodel_symbol(eaglemodel_Symbol eaglemodel_symbol) {
        this.eaglemodel_symbol = eaglemodel_symbol;
    }
    public eaglemodel_Sheet getEaglemodel_sheet() {
        return eaglemodel_sheet;
    }

    public void setEaglemodel_sheet(eaglemodel_Sheet eaglemodel_sheet) {
        this.eaglemodel_sheet = eaglemodel_sheet;
    }
    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }
    public eaglemodel_Deviceset getEaglemodel_deviceset() {
        return eaglemodel_deviceset;
    }

    public void setEaglemodel_deviceset(eaglemodel_Deviceset eaglemodel_deviceset) {
        this.eaglemodel_deviceset = eaglemodel_deviceset;
    }
    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }

}