





import java.util.List;
import java.util.ArrayList;

public class connection_HeaderFooterConnection extends Connection {

    private String imports;
    private String libraries;
    private boolean isHeader;
    private String mainCode;



    public connection_HeaderFooterConnection(
        String imports,        String libraries,        boolean isHeader,        String mainCode    ) {
        super(
        );
        this.imports = imports;
        this.libraries = libraries;
        this.isHeader = isHeader;
        this.mainCode = mainCode;
    }


    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getLibraries() {
        return libraries;
    }

    public void setLibraries(String libraries) {
        this.libraries = libraries;
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