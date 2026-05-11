





import java.util.List;
import java.util.ArrayList;

public class website_UnitField  {

    private int maximumDisplaySize;
    private String dateFormat;
    private String collectionDisplayOption;
    private boolean collectionAllowAdd;
    private String title;
    private boolean collectionAllowRemove;





    private website_InterfaceField website_interfacefield;


    public website_UnitField(
        int maximumDisplaySize,        String dateFormat,        String collectionDisplayOption,        boolean collectionAllowAdd,        String title,        boolean collectionAllowRemove    ) {
        this.maximumDisplaySize = maximumDisplaySize;
        this.dateFormat = dateFormat;
        this.collectionDisplayOption = collectionDisplayOption;
        this.collectionAllowAdd = collectionAllowAdd;
        this.title = title;
        this.collectionAllowRemove = collectionAllowRemove;
    }


    public int getMaximumdisplaysize() {
        return maximumDisplaySize;
    }

    public void setMaximumdisplaysize(int maximumDisplaySize) {
        this.maximumDisplaySize = maximumDisplaySize;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }
    public String getCollectiondisplayoption() {
        return collectionDisplayOption;
    }

    public void setCollectiondisplayoption(String collectionDisplayOption) {
        this.collectionDisplayOption = collectionDisplayOption;
    }
    public boolean getCollectionallowadd() {
        return collectionAllowAdd;
    }

    public void setCollectionallowadd(boolean collectionAllowAdd) {
        this.collectionAllowAdd = collectionAllowAdd;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getCollectionallowremove() {
        return collectionAllowRemove;
    }

    public void setCollectionallowremove(boolean collectionAllowRemove) {
        this.collectionAllowRemove = collectionAllowRemove;
    }

    public website_InterfaceField getWebsite_interfacefield() {
        return website_interfacefield;
    }

    public void setWebsite_interfacefield(website_InterfaceField website_interfacefield) {
        this.website_interfacefield = website_interfacefield;
    }

}