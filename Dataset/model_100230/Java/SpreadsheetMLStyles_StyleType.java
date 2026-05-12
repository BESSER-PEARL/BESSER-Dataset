





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_StyleType  {

    private String id;
    private String name;





    private StyleType styletype;




    private StyledElement styledelement;




    private StyleType styletype;




    private StylesCollection stylescollection;


    public SpreadsheetMLStyles_StyleType(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }
    public StyledElement getStyledelement() {
        return styledelement;
    }

    public void setStyledelement(StyledElement styledelement) {
        this.styledelement = styledelement;
    }
    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }
    public StylesCollection getStylescollection() {
        return stylescollection;
    }

    public void setStylescollection(StylesCollection stylescollection) {
        this.stylescollection = stylescollection;
    }

}