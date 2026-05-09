





import java.util.List;
import java.util.ArrayList;

public class library_NetXResource  {

    private String expressionName;
    private String longName;
    private String detailDisplay;
    private String summaryDisplay;
    private String shortName;





    private library_Equipment library_equipment;




    private library_Equipment library_equipment;




    private library_EquipmentGroup library_equipmentgroup;




    private library_EquipmentGroup library_equipmentgroup;


    public library_NetXResource(
        String expressionName,        String longName,        String detailDisplay,        String summaryDisplay,        String shortName    ) {
        this.expressionName = expressionName;
        this.longName = longName;
        this.detailDisplay = detailDisplay;
        this.summaryDisplay = summaryDisplay;
        this.shortName = shortName;
    }


    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }
    public String getDetaildisplay() {
        return detailDisplay;
    }

    public void setDetaildisplay(String detailDisplay) {
        this.detailDisplay = detailDisplay;
    }
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }

    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }
    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }

}