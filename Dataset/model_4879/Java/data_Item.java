




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Item  {

    private String ident;
    private LocalDate created;
    private String uri;
    private String stringValue;
    private LocalDate lastModified;





    private data_Identifier data_identifier;




    private List<data_Item> data_items;




    private List<data_Identifier> data_identifiers;




    private data_DataSet data_dataset;




    private data_Item data_item;




    private data_MetaTag data_metatag;




    private List<data_MetaTag> data_metatags;




    private data_DataSet data_dataset;


    public data_Item(
        String ident,        LocalDate created,        String uri,        String stringValue,        LocalDate lastModified    ) {
        this.ident = ident;
        this.created = created;
        this.uri = uri;
        this.stringValue = stringValue;
        this.lastModified = lastModified;
        this.data_items = new ArrayList<>();
        this.data_identifiers = new ArrayList<>();
        this.data_metatags = new ArrayList<>();
    }

    public data_Item(
        String ident,        LocalDate created,        String uri,        String stringValue,        LocalDate lastModified        ArrayList<data_Item> data_items,        ArrayList<data_Identifier> data_identifiers,        ArrayList<data_MetaTag> data_metatags    ) {
        this.ident = ident;
        this.created = created;
        this.uri = uri;
        this.stringValue = stringValue;
        this.lastModified = lastModified;
        this.data_items = data_items;
        this.data_identifiers = data_identifiers;
        this.data_metatags = data_metatags;
    }

    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }

    public data_Identifier getData_identifier() {
        return data_identifier;
    }

    public void setData_identifier(data_Identifier data_identifier) {
        this.data_identifier = data_identifier;
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
    public data_DataSet getData_dataset() {
        return data_dataset;
    }

    public void setData_dataset(data_DataSet data_dataset) {
        this.data_dataset = data_dataset;
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

}