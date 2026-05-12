





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private boolean UseHeader;
    private String FooterValue;
    private String RowSeparatorType;
    private String Encoding;
    private boolean RemoveEmptyRow;
    private boolean CsvOption;
    private String FilePath;
    private String RowSeparatorValue;
    private boolean UseFooter;
    private String TextEnclosure;
    private boolean UseLimit;
    private String EscapeType;
    private String TextIdentifier;
    private String LimitValue;
    private String Server;
    private String EscapeChar;
    private String FieldSeparatorValue;
    private String Format;
    private boolean FirstLineCaption;
    private String HeaderValue;



    public connection_FileConnection(
        boolean UseHeader,        String FooterValue,        String RowSeparatorType,        String Encoding,        boolean RemoveEmptyRow,        boolean CsvOption,        String FilePath,        String RowSeparatorValue,        boolean UseFooter,        String TextEnclosure,        boolean UseLimit,        String EscapeType,        String TextIdentifier,        String LimitValue,        String Server,        String EscapeChar,        String FieldSeparatorValue,        String Format,        boolean FirstLineCaption,        String HeaderValue    ) {
        super(
        );
        this.UseHeader = UseHeader;
        this.FooterValue = FooterValue;
        this.RowSeparatorType = RowSeparatorType;
        this.Encoding = Encoding;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.CsvOption = CsvOption;
        this.FilePath = FilePath;
        this.RowSeparatorValue = RowSeparatorValue;
        this.UseFooter = UseFooter;
        this.TextEnclosure = TextEnclosure;
        this.UseLimit = UseLimit;
        this.EscapeType = EscapeType;
        this.TextIdentifier = TextIdentifier;
        this.LimitValue = LimitValue;
        this.Server = Server;
        this.EscapeChar = EscapeChar;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.Format = Format;
        this.FirstLineCaption = FirstLineCaption;
        this.HeaderValue = HeaderValue;
    }


    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public String getRowseparatortype() {
        return RowSeparatorType;
    }

    public void setRowseparatortype(String RowSeparatorType) {
        this.RowSeparatorType = RowSeparatorType;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public boolean getRemoveemptyrow() {
        return RemoveEmptyRow;
    }

    public void setRemoveemptyrow(boolean RemoveEmptyRow) {
        this.RemoveEmptyRow = RemoveEmptyRow;
    }
    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getRowseparatorvalue() {
        return RowSeparatorValue;
    }

    public void setRowseparatorvalue(String RowSeparatorValue) {
        this.RowSeparatorValue = RowSeparatorValue;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public String getFieldseparatorvalue() {
        return FieldSeparatorValue;
    }

    public void setFieldseparatorvalue(String FieldSeparatorValue) {
        this.FieldSeparatorValue = FieldSeparatorValue;
    }
    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }
    public String getHeadervalue() {
        return HeaderValue;
    }

    public void setHeadervalue(String HeaderValue) {
        this.HeaderValue = HeaderValue;
    }


}