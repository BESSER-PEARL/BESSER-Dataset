





import java.util.List;
import java.util.ArrayList;

public class beans_BeanProperty extends NamedElement {

    private String typeName;
    private boolean changeable;





    private beans_Bean beans_bean;




    private beans_Bean beans_bean;


    public beans_BeanProperty(
        String typeName,        boolean changeable    ) {
        super(
        );
        this.typeName = typeName;
        this.changeable = changeable;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }

    public beans_Bean getBeans_bean() {
        return beans_bean;
    }

    public void setBeans_bean(beans_Bean beans_bean) {
        this.beans_bean = beans_bean;
    }
    public beans_Bean getBeans_bean() {
        return beans_bean;
    }

    public void setBeans_bean(beans_Bean beans_bean) {
        this.beans_bean = beans_bean;
    }

}