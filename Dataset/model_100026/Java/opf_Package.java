





import java.util.List;
import java.util.ArrayList;

public class opf_Package  {

    private boolean generateTableOfContents;
    private String uniqueIdentifier;
    private String version;
    private boolean generateCoverHTML;
    private boolean includeReferencedResources;



    public opf_Package(
        boolean generateTableOfContents,        String uniqueIdentifier,        String version,        boolean generateCoverHTML,        boolean includeReferencedResources    ) {
        this.generateTableOfContents = generateTableOfContents;
        this.uniqueIdentifier = uniqueIdentifier;
        this.version = version;
        this.generateCoverHTML = generateCoverHTML;
        this.includeReferencedResources = includeReferencedResources;
    }


    public boolean getGeneratetableofcontents() {
        return generateTableOfContents;
    }

    public void setGeneratetableofcontents(boolean generateTableOfContents) {
        this.generateTableOfContents = generateTableOfContents;
    }
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getGeneratecoverhtml() {
        return generateCoverHTML;
    }

    public void setGeneratecoverhtml(boolean generateCoverHTML) {
        this.generateCoverHTML = generateCoverHTML;
    }
    public boolean getIncludereferencedresources() {
        return includeReferencedResources;
    }

    public void setIncludereferencedresources(boolean includeReferencedResources) {
        this.includeReferencedResources = includeReferencedResources;
    }


}