





import java.util.List;
import java.util.ArrayList;

public class opf_Package  {

    private boolean generateTableOfContents;
    private String lang;
    private boolean includeReferencedResources;
    private String version;
    private String uniqueIdentifier;
    private String prefix;
    private String dir;
    private String id;
    private boolean generateCoverHTML;



    public opf_Package(
        boolean generateTableOfContents,        String lang,        boolean includeReferencedResources,        String version,        String uniqueIdentifier,        String prefix,        String dir,        String id,        boolean generateCoverHTML    ) {
        this.generateTableOfContents = generateTableOfContents;
        this.lang = lang;
        this.includeReferencedResources = includeReferencedResources;
        this.version = version;
        this.uniqueIdentifier = uniqueIdentifier;
        this.prefix = prefix;
        this.dir = dir;
        this.id = id;
        this.generateCoverHTML = generateCoverHTML;
    }


    public boolean getGeneratetableofcontents() {
        return generateTableOfContents;
    }

    public void setGeneratetableofcontents(boolean generateTableOfContents) {
        this.generateTableOfContents = generateTableOfContents;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public boolean getIncludereferencedresources() {
        return includeReferencedResources;
    }

    public void setIncludereferencedresources(boolean includeReferencedResources) {
        this.includeReferencedResources = includeReferencedResources;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getGeneratecoverhtml() {
        return generateCoverHTML;
    }

    public void setGeneratecoverhtml(boolean generateCoverHTML) {
        this.generateCoverHTML = generateCoverHTML;
    }


}