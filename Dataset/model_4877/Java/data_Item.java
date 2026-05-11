




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Item  {

    private LocalDate created;
    private String stringValue;
    private String ident;
    private String uri;
    private LocalDate lastModified;





    private data_DataSet data_dataset;




    private data_DataSet data_dataset;




    private data_Item data_item;




    private data_Identifier data_identifier;




    private data_Item data_item;




    private data_Item data_item;




    private data_MetaTag data_metatag;




    private List<data_Identifier> data_identifiers;




    private List<data_Item> data_items;




    private List<data_MetaTag> data_metatags;


    public data_Item(
        LocalDate created,        String stringValue,        String ident,        String uri,        LocalDate lastModified    ) {
        this.created = created;
        this.stringValue = stringValue;
        this.ident = ident;
        this.uri = uri;
        this.lastModified = lastModified;
        this.data_identifiers = new ArrayList<>();
        this.data_items = new ArrayList<>();
        this.data_metatags = new ArrayList<>();
    }

    public data_Item(
        LocalDate created,        String stringValue,        String ident,        String uri,        LocalDate lastModified        ArrayList<data_Identifier> data_identifiers,        ArrayList<data_Item> data_items,        ArrayList<data_MetaTag> data_metatags    ) {
        this.created = created;
        this.stringValue = stringValue;
        this.ident = ident;
        this.uri = uri;
        this.lastModified = lastModified;
        this.data_identifiers = data_identifiers;
        this.data_items = data_items;
        this.data_metatags = data_metatags;
    }

    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }
    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }

    public data_DataSet getData_dataset() {
        return data_dataset;
    }

    public void setData_dataset(data_DataSet data_dataset) {
        this.data_dataset = data_dataset;
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
    public List<data_Identifier> getData_identifiers() {
        return data_identifiers;
    }

    public void addData_identifier(Data_identifier data_identifier) {
        this.data_identifiers.add(data_identifier);
    }
    public List<data_Item> getData_items() {
        return data_items;
    }

    public void addData_item(Data_item data_item) {
        this.data_items.add(data_item);
    }
    public List<data_MetaTag> getData_metatags() {
        return data_metatags;
    }

    public void addData_metatag(Data_metatag data_metatag) {
        this.data_metatags.add(data_metatag);
    }

}