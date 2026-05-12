





import java.util.List;
import java.util.ArrayList;

public class connection_HeaderFooterConnection extends Connection {

    private String libraries;
    private String mainCode;
    private boolean isHeader;
    private String imports;



    public connection_HeaderFooterConnection(
        String libraries,        String mainCode,        boolean isHeader,        String imports    ) {
        super(
        );
        this.libraries = libraries;
        this.mainCode = mainCode;
        this.isHeader = isHeader;
        this.imports = imports;
    }


    public String getLibraries() {
        return libraries;
    }

    public void setLibraries(String libraries) {
        this.libraries = libraries;
    }
    public String getMaincode() {
        return mainCode;
    }

    public void setMaincode(String mainCode) {
        this.mainCode = mainCode;
    }
    public boolean getIsheader() {
        return isHeader;
    }

    public void setIsheader(boolean isHeader) {
        this.isHeader = isHeader;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }


}