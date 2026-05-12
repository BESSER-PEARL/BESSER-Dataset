





import java.util.List;
import java.util.ArrayList;

public class xdoc_GlossaryEntry  {

    private String alias;
    private String name;





    private List<xdoc_TextOrMarkup> xdoc_textormarkups;




    private xdoc_Glossary xdoc_glossary;


    public xdoc_GlossaryEntry(
        String alias,        String name    ) {
        this.alias = alias;
        this.name = name;
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_GlossaryEntry(
        String alias,        String name        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.alias = alias;
        this.name = name;
        this.xdoc_textormarkups = xdoc_textormarkups;
    }

    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }
    public xdoc_Glossary getXdoc_glossary() {
        return xdoc_glossary;
    }

    public void setXdoc_glossary(xdoc_Glossary xdoc_glossary) {
        this.xdoc_glossary = xdoc_glossary;
    }

}