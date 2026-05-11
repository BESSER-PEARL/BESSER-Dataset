




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Item  {

    private String uri;
    private LocalDate created;
    private LocalDate lastModified;
    private String ident;
    private String stringXML;
    private String stringValue;





    private data_Item data_item;




    private data_MetaTag data_metatag;




    private data_DataSet data_dataset;




    private List<data_MetaTag> data_metatags;




    private data_DataSet data_dataset;




    private List<data_Item> data_items;




    private data_Identifier data_identifier;




    private data_Item data_item;




    private List<data_Item> data_items;




    private List<data_Identifier> data_identifiers;


    public data_Item(
        String uri,        LocalDate created,        LocalDate lastModified,        String ident,        String stringXML,        String stringValue    ) {
        this.uri = uri;
        this.created = created;
        this.lastModified = lastModified;
        this.ident = ident;
        this.stringXML = stringXML;
        this.stringValue = stringValue;
        this.data_metatags = new ArrayList<>();
        this.data_items = new ArrayList<>();
        this.data_items = new ArrayList<>();
        this.data_identifiers = new ArrayList<>();
    }

    public data_Item(
        String uri,        LocalDate created,        LocalDate lastModified,        String ident,        String stringXML,        String stringValue        ArrayList<data_MetaTag> data_metatags,        ArrayList<data_Item> data_items,        ArrayList<data_Item> data_items,        ArrayList<data_Identifier> data_identifiers    ) {
        this.uri = uri;
        this.created = created;
        this.lastModified = lastModified;
        this.ident = ident;
        this.stringXML = stringXML;
        this.stringValue = stringValue;
        this.data_metatags = data_metatags;
        this.data_items = data_items;
        this.data_items = data_items;
        this.data_identifiers = data_identifiers;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getStringxml() {
        return stringXML;
    }

    public void setStringxml(String stringXML) {
        this.stringXML = stringXML;
    }
    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }

    public data_Item getData_item() {
        return data_item;
    }

    public void setData_item(data_Item data_item) {
        this.data_item = data_item;
    }
    public data_MetaTag getData_metatag() {
        return data_metatag;
    }

    public void setData_metatag(data_MetaTag data_metatag) {
        this.data_metatag = data_metatag;
    }
    public data_DataSet getData_dataset() {
        return data_dataset;
    }

    public void setData_dataset(data_DataSet data_dataset) {
        this.data_dataset = data_dataset;
    }
    public List<data_MetaTag> getData_metatags() {
        return data_metatags;
    }

    public void addData_metatag(Data_metatag data_metatag) {
        this.data_metatags.add(data_metatag);
    }
    public data_DataSet getData_dataset() {
        return data_dataset;
    }

    public void setData_dataset(data_DataSet data_dataset) {
        this.data_dataset = data_dataset;
    }
    public List<data_Item> getData_items() {
        return data_items;
    }

    public void addData_item(Data_item data_item) {
        this.data_items.add(data_item);
    }
    public data_Identifier getData_identifier() {
        return data_identifier;
    }

    public void setData_identifier(data_Identifier data_identifier) {
        this.data_identifier = data_identifier;
    }
    public data_Item getData_item() {
        return data_item;
    }

    public void setData_item(data_Item data_item) {
        this.data_item = data_item;
    }
    public List<data_Item> getData_items() {
        return data_items;
    }

    public void addData_item(Data_item data_item) {
        this.data_items.add(data_item);
    }
    public List<data_Identifier> getData_identifiers() {
        return data_identifiers;
    }

    public void addData_identifier(Data_identifier data_identifier) {
        this.data_identifiers.add(data_identifier);
    }

}