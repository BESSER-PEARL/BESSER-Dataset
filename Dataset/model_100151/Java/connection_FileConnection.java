





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private String EscapeType;
    private String RowSeparatorValue;
    private boolean UseLimit;
    private String Encoding;
    private boolean UseHeader;
    private String LimitValue;
    private boolean RemoveEmptyRow;
    private String Server;
    private String FooterValue;
    private String EscapeChar;
    private boolean FirstLineCaption;
    private String FieldSeparatorValue;
    private String HeaderValue;
    private String TextEnclosure;
    private String Format;
    private String TextIdentifier;
    private boolean UseFooter;
    private String FilePath;
    private String RowSeparatorType;
    private boolean CsvOption;



    public connection_FileConnection(
        String EscapeType,        String RowSeparatorValue,        boolean UseLimit,        String Encoding,        boolean UseHeader,        String LimitValue,        boolean RemoveEmptyRow,        String Server,        String FooterValue,        String EscapeChar,        boolean FirstLineCaption,        String FieldSeparatorValue,        String HeaderValue,        String TextEnclosure,        String Format,        String TextIdentifier,        boolean UseFooter,        String FilePath,        String RowSeparatorType,        boolean CsvOption    ) {
        super(
        );
        this.EscapeType = EscapeType;
        this.RowSeparatorValue = RowSeparatorValue;
        this.UseLimit = UseLimit;
        this.Encoding = Encoding;
        this.UseHeader = UseHeader;
        this.LimitValue = LimitValue;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.Server = Server;
        this.FooterValue = FooterValue;
        this.EscapeChar = EscapeChar;
        this.FirstLineCaption = FirstLineCaption;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.HeaderValue = HeaderValue;
        this.TextEnclosure = TextEnclosure;
        this.Format = Format;
        this.TextIdentifier = TextIdentifier;
        this.UseFooter = UseFooter;
        this.FilePath = FilePath;
        this.RowSeparatorType = RowSeparatorType;
        this.CsvOption = CsvOption;
    }


    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
    }
    public String getRowseparatorvalue() {
        return RowSeparatorValue;
    }

    public void setRowseparatorvalue(String RowSeparatorValue) {
        this.RowSeparatorValue = RowSeparatorValue;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public boolean getRemoveemptyrow() {
        return RemoveEmptyRow;
    }

    public void setRemoveemptyrow(boolean RemoveEmptyRow) {
        this.RemoveEmptyRow = RemoveEmptyRow;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }
    public String getFieldseparatorvalue() {
        return FieldSeparatorValue;
    }

    public void setFieldseparatorvalue(String FieldSeparatorValue) {
        this.FieldSeparatorValue = FieldSeparatorValue;
    }
    public String getHeadervalue() {
        return HeaderValue;
    }

    public void setHeadervalue(String HeaderValue) {
        this.HeaderValue = HeaderValue;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
    }
    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getRowseparatortype() {
        return RowSeparatorType;
    }

    public void setRowseparatortype(String RowSeparatorType) {
        this.RowSeparatorType = RowSeparatorType;
    }
    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
    }


}