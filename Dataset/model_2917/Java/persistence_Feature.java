





import java.util.List;
import java.util.ArrayList;

public class persistence_Feature  {

    private boolean encodeUriKey;
    private String headerClass;
    private boolean collectionAllowRemove;
    private String displayClass;
    private String nullDisplayValue;
    private String title;
    private boolean collectionAllowAdd;
    private String footerClass;





    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private List<persistence_SerializationGroup> persistence_serializationgroups;


    public persistence_Feature(
        boolean encodeUriKey,        String headerClass,        boolean collectionAllowRemove,        String displayClass,        String nullDisplayValue,        String title,        boolean collectionAllowAdd,        String footerClass    ) {
        this.encodeUriKey = encodeUriKey;
        this.headerClass = headerClass;
        this.collectionAllowRemove = collectionAllowRemove;
        this.displayClass = displayClass;
        this.nullDisplayValue = nullDisplayValue;
        this.title = title;
        this.collectionAllowAdd = collectionAllowAdd;
        this.footerClass = footerClass;
        this.persistence_serializationgroups = new ArrayList<>();
    }

    public persistence_Feature(
        boolean encodeUriKey,        String headerClass,        boolean collectionAllowRemove,        String displayClass,        String nullDisplayValue,        String title,        boolean collectionAllowAdd,        String footerClass        ArrayList<persistence_SerializationGroup> persistence_serializationgroups    ) {
        this.encodeUriKey = encodeUriKey;
        this.headerClass = headerClass;
        this.collectionAllowRemove = collectionAllowRemove;
        this.displayClass = displayClass;
        this.nullDisplayValue = nullDisplayValue;
        this.title = title;
        this.collectionAllowAdd = collectionAllowAdd;
        this.footerClass = footerClass;
        this.persistence_serializationgroups = persistence_serializationgroups;
    }

    public boolean getEncodeurikey() {
        return encodeUriKey;
    }

    public void setEncodeurikey(boolean encodeUriKey) {
        this.encodeUriKey = encodeUriKey;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }
    public boolean getCollectionallowremove() {
        return collectionAllowRemove;
    }

    public void setCollectionallowremove(boolean collectionAllowRemove) {
        this.collectionAllowRemove = collectionAllowRemove;
    }
    public String getDisplayclass() {
        return displayClass;
    }

    public void setDisplayclass(String displayClass) {
        this.displayClass = displayClass;
    }
    public String getNulldisplayvalue() {
        return nullDisplayValue;
    }

    public void setNulldisplayvalue(String nullDisplayValue) {
        this.nullDisplayValue = nullDisplayValue;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getCollectionallowadd() {
        return collectionAllowAdd;
    }

    public void setCollectionallowadd(boolean collectionAllowAdd) {
        this.collectionAllowAdd = collectionAllowAdd;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }

    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public List<persistence_SerializationGroup> getPersistence_serializationgroups() {
        return persistence_serializationgroups;
    }

    public void addPersistence_serializationgroup(Persistence_serializationgroup persistence_serializationgroup) {
        this.persistence_serializationgroups.add(persistence_serializationgroup);
    }

}