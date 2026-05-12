





import java.util.List;
import java.util.ArrayList;

public class connection_HeaderFooterConnection extends Connection {

    private String libraries;
    private String imports;
    private boolean isHeader;
    private String mainCode;



    public connection_HeaderFooterConnection(
        String libraries,        String imports,        boolean isHeader,        String mainCode    ) {
        super(
        );
        this.libraries = libraries;
        this.imports = imports;
        this.isHeader = isHeader;
        this.mainCode = mainCode;
    }


    public String getLibraries() {
        return libraries;
    }

    public void setLibraries(String libraries) {
        this.libraries = libraries;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public boolean getIsheader() {
        return isHeader;
    }

    public void setIsheader(boolean isHeader) {
        this.isHeader = isHeader;
    }
    public String getMaincode() {
        return mainCode;
    }

    public void setMaincode(String mainCode) {
        this.mainCode = mainCode;
    }


}