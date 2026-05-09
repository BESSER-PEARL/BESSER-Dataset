





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_AbstractRepresentation  {

    private String viewFactory;
    private String name;
    private String editPartQualifiedName;



    public expansionmodel_AbstractRepresentation(
        String viewFactory,        String name,        String editPartQualifiedName    ) {
        this.viewFactory = viewFactory;
        this.name = name;
        this.editPartQualifiedName = editPartQualifiedName;
    }


    public String getViewfactory() {
        return viewFactory;
    }

    public void setViewfactory(String viewFactory) {
        this.viewFactory = viewFactory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEditpartqualifiedname() {
        return editPartQualifiedName;
    }

    public void setEditpartqualifiedname(String editPartQualifiedName) {
        this.editPartQualifiedName = editPartQualifiedName;
    }


}