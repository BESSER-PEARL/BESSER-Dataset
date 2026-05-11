





import java.util.List;
import java.util.ArrayList;

public class krendering_KCustomRendering extends KContainerRendering {

    private String figureObject;
    private String bundleName;
    private String className;



    public krendering_KCustomRendering(
        String figureObject,        String bundleName,        String className    ) {
        super(
        );
        this.figureObject = figureObject;
        this.bundleName = bundleName;
        this.className = className;
    }


    public String getFigureobject() {
        return figureObject;
    }

    public void setFigureobject(String figureObject) {
        this.figureObject = figureObject;
    }
    public String getBundlename() {
        return bundleName;
    }

    public void setBundlename(String bundleName) {
        this.bundleName = bundleName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}