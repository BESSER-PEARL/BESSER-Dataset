





import java.util.List;
import java.util.ArrayList;

public class krendering_KCustomRendering extends KContainerRendering {

    private String className;
    private String bundleName;
    private String figureObject;



    public krendering_KCustomRendering(
        String className,        String bundleName,        String figureObject    ) {
        super(
        );
        this.className = className;
        this.bundleName = bundleName;
        this.figureObject = figureObject;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getBundlename() {
        return bundleName;
    }

    public void setBundlename(String bundleName) {
        this.bundleName = bundleName;
    }
    public String getFigureobject() {
        return figureObject;
    }

    public void setFigureobject(String figureObject) {
        this.figureObject = figureObject;
    }


}