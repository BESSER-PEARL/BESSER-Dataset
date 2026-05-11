





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ContentProvider extends ModelElement {

    private boolean many;
    private String name;
    private boolean html;
    private boolean xml;
    private boolean resolver;





    private applauseDsl_Type applausedsl_type;


    public applauseDsl_ContentProvider(
        boolean many,        String name,        boolean html,        boolean xml,        boolean resolver    ) {
        super(
        );
        this.many = many;
        this.name = name;
        this.html = html;
        this.xml = xml;
        this.resolver = resolver;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getHtml() {
        return html;
    }

    public void setHtml(boolean html) {
        this.html = html;
    }
    public boolean getXml() {
        return xml;
    }

    public void setXml(boolean xml) {
        this.xml = xml;
    }
    public boolean getResolver() {
        return resolver;
    }

    public void setResolver(boolean resolver) {
        this.resolver = resolver;
    }

    public applauseDsl_Type getApplausedsl_type() {
        return applausedsl_type;
    }

    public void setApplausedsl_type(applauseDsl_Type applausedsl_type) {
        this.applausedsl_type = applausedsl_type;
    }

}