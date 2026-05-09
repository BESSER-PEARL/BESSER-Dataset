




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class oaam_common_OaamBaseElementA  {

    private String traceLink;
    private String modifier;
    private String documentation;
    private LocalDate modified;
    private String name;
    private String style;
    private String id;



    public oaam_common_OaamBaseElementA(
        String traceLink,        String modifier,        String documentation,        LocalDate modified,        String name,        String style,        String id    ) {
        this.traceLink = traceLink;
        this.modifier = modifier;
        this.documentation = documentation;
        this.modified = modified;
        this.name = name;
        this.style = style;
        this.id = id;
    }


    public String getTracelink() {
        return traceLink;
    }

    public void setTracelink(String traceLink) {
        this.traceLink = traceLink;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public LocalDate getModified() {
        return modified;
    }

    public void setModified(LocalDate modified) {
        this.modified = modified;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}