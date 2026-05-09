





import java.util.List;
import java.util.ArrayList;

public class QVTTemplate_PropertyTemplateItem extends Element {

    private String isOpposite;





    private Property property;


    public QVTTemplate_PropertyTemplateItem(
        String isOpposite    ) {
        super(
        );
        this.isOpposite = isOpposite;
    }


    public String getIsopposite() {
        return isOpposite;
    }

    public void setIsopposite(String isOpposite) {
        this.isOpposite = isOpposite;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}