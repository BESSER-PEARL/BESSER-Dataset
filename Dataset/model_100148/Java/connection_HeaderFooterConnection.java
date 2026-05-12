





import java.util.List;
import java.util.ArrayList;

public class connection_HeaderFooterConnection extends Connection {

    private boolean isHeader;
    private String libraries;
    private String imports;
    private String mainCode;



    public connection_HeaderFooterConnection(
        boolean isHeader,        String libraries,        String imports,        String mainCode    ) {
        super(
        );
        this.isHeader = isHeader;
        this.libraries = libraries;
        this.imports = imports;
        this.mainCode = mainCode;
    }


    public boolean getIsheader() {
        return isHeader;
    }

    public void setIsheader(boolean isHeader) {
        this.isHeader = isHeader;
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
    public String getMaincode() {
        return mainCode;
    }

    public void setMaincode(String mainCode) {
        this.mainCode = mainCode;
    }


}