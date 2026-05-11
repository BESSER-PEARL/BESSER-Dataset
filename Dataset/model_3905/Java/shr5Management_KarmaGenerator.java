





import java.util.List;
import java.util.ArrayList;

public class shr5Management_KarmaGenerator  {

    private int karmaToResource;
    private int resourceSpend;
    private int choiseKarmaCost;
    private int startResources;
    private int startKarma;
    private int karmaSpend;





    private shr5Management_SpecialType shr5management_specialtype;


    public shr5Management_KarmaGenerator(
        int karmaToResource,        int resourceSpend,        int choiseKarmaCost,        int startResources,        int startKarma,        int karmaSpend    ) {
        this.karmaToResource = karmaToResource;
        this.resourceSpend = resourceSpend;
        this.choiseKarmaCost = choiseKarmaCost;
        this.startResources = startResources;
        this.startKarma = startKarma;
        this.karmaSpend = karmaSpend;
    }


    public int getKarmatoresource() {
        return karmaToResource;
    }

    public void setKarmatoresource(int karmaToResource) {
        this.karmaToResource = karmaToResource;
    }
    public int getResourcespend() {
        return resourceSpend;
    }

    public void setResourcespend(int resourceSpend) {
        this.resourceSpend = resourceSpend;
    }
    public int getChoisekarmacost() {
        return choiseKarmaCost;
    }

    public void setChoisekarmacost(int choiseKarmaCost) {
        this.choiseKarmaCost = choiseKarmaCost;
    }
    public int getStartresources() {
        return startResources;
    }

    public void setStartresources(int startResources) {
        this.startResources = startResources;
    }
    public int getStartkarma() {
        return startKarma;
    }

    public void setStartkarma(int startKarma) {
        this.startKarma = startKarma;
    }
    public int getKarmaspend() {
        return karmaSpend;
    }

    public void setKarmaspend(int karmaSpend) {
        this.karmaSpend = karmaSpend;
    }

    public shr5Management_SpecialType getShr5management_specialtype() {
        return shr5management_specialtype;
    }

    public void setShr5management_specialtype(shr5Management_SpecialType shr5management_specialtype) {
        this.shr5management_specialtype = shr5management_specialtype;
    }

}