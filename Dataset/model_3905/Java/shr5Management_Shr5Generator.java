





import java.util.List;
import java.util.ArrayList;

public class shr5Management_Shr5Generator  {

    private int spellPointSpend;
    private int resourceSpend;
    private int connectionSpend;
    private int karmaToResource;
    private int skillPointSpend;
    private int startKarma;
    private int specialPointSpend;
    private int startResources;
    private int attributeSpend;
    private int karmaSpend;
    private int groupPointSpend;
    private int knownlegePointSpend;





    private shr5Management_SpecialType shr5management_specialtype;




    private shr5Management_Skill shr5management_skill;




    private shr5Management_Attributes shr5management_attributes;




    private shr5Management_Resourcen shr5management_resourcen;


    public shr5Management_Shr5Generator(
        int spellPointSpend,        int resourceSpend,        int connectionSpend,        int karmaToResource,        int skillPointSpend,        int startKarma,        int specialPointSpend,        int startResources,        int attributeSpend,        int karmaSpend,        int groupPointSpend,        int knownlegePointSpend    ) {
        this.spellPointSpend = spellPointSpend;
        this.resourceSpend = resourceSpend;
        this.connectionSpend = connectionSpend;
        this.karmaToResource = karmaToResource;
        this.skillPointSpend = skillPointSpend;
        this.startKarma = startKarma;
        this.specialPointSpend = specialPointSpend;
        this.startResources = startResources;
        this.attributeSpend = attributeSpend;
        this.karmaSpend = karmaSpend;
        this.groupPointSpend = groupPointSpend;
        this.knownlegePointSpend = knownlegePointSpend;
    }


    public int getSpellpointspend() {
        return spellPointSpend;
    }

    public void setSpellpointspend(int spellPointSpend) {
        this.spellPointSpend = spellPointSpend;
    }
    public int getResourcespend() {
        return resourceSpend;
    }

    public void setResourcespend(int resourceSpend) {
        this.resourceSpend = resourceSpend;
    }
    public int getConnectionspend() {
        return connectionSpend;
    }

    public void setConnectionspend(int connectionSpend) {
        this.connectionSpend = connectionSpend;
    }
    public int getKarmatoresource() {
        return karmaToResource;
    }

    public void setKarmatoresource(int karmaToResource) {
        this.karmaToResource = karmaToResource;
    }
    public int getSkillpointspend() {
        return skillPointSpend;
    }

    public void setSkillpointspend(int skillPointSpend) {
        this.skillPointSpend = skillPointSpend;
    }
    public int getStartkarma() {
        return startKarma;
    }

    public void setStartkarma(int startKarma) {
        this.startKarma = startKarma;
    }
    public int getSpecialpointspend() {
        return specialPointSpend;
    }

    public void setSpecialpointspend(int specialPointSpend) {
        this.specialPointSpend = specialPointSpend;
    }
    public int getStartresources() {
        return startResources;
    }

    public void setStartresources(int startResources) {
        this.startResources = startResources;
    }
    public int getAttributespend() {
        return attributeSpend;
    }

    public void setAttributespend(int attributeSpend) {
        this.attributeSpend = attributeSpend;
    }
    public int getKarmaspend() {
        return karmaSpend;
    }

    public void setKarmaspend(int karmaSpend) {
        this.karmaSpend = karmaSpend;
    }
    public int getGrouppointspend() {
        return groupPointSpend;
    }

    public void setGrouppointspend(int groupPointSpend) {
        this.groupPointSpend = groupPointSpend;
    }
    public int getKnownlegepointspend() {
        return knownlegePointSpend;
    }

    public void setKnownlegepointspend(int knownlegePointSpend) {
        this.knownlegePointSpend = knownlegePointSpend;
    }

    public shr5Management_SpecialType getShr5management_specialtype() {
        return shr5management_specialtype;
    }

    public void setShr5management_specialtype(shr5Management_SpecialType shr5management_specialtype) {
        this.shr5management_specialtype = shr5management_specialtype;
    }
    public shr5Management_Skill getShr5management_skill() {
        return shr5management_skill;
    }

    public void setShr5management_skill(shr5Management_Skill shr5management_skill) {
        this.shr5management_skill = shr5management_skill;
    }
    public shr5Management_Attributes getShr5management_attributes() {
        return shr5management_attributes;
    }

    public void setShr5management_attributes(shr5Management_Attributes shr5management_attributes) {
        this.shr5management_attributes = shr5management_attributes;
    }
    public shr5Management_Resourcen getShr5management_resourcen() {
        return shr5management_resourcen;
    }

    public void setShr5management_resourcen(shr5Management_Resourcen shr5management_resourcen) {
        this.shr5management_resourcen = shr5management_resourcen;
    }

}