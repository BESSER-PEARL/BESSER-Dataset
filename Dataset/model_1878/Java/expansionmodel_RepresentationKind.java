





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_RepresentationKind  {

    private String viewFactory;
    private String name;
    private String editPartQualifiedName;





    private expansionmodel_AbstractRepresentation expansionmodel_abstractrepresentation;


    public expansionmodel_RepresentationKind(
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

    public expansionmodel_AbstractRepresentation getExpansionmodel_abstractrepresentation() {
        return expansionmodel_abstractrepresentation;
    }

    public void setExpansionmodel_abstractrepresentation(expansionmodel_AbstractRepresentation expansionmodel_abstractrepresentation) {
        this.expansionmodel_abstractrepresentation = expansionmodel_abstractrepresentation;
    }

}