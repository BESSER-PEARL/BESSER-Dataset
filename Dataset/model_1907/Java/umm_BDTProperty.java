





import java.util.List;
import java.util.ArrayList;

public class umm_BDTProperty extends OclRef {

    private String dictionary;
    private String uniqueIdentifier;
    private int maxLength;
    private String versionIdentifier;
    private int minLength;
    private int length;
    private String definition;
    private String pattern;
    private String businessTerm;





    private umm_BDT umm_bdt;


    public umm_BDTProperty(
        String dictionary,        String uniqueIdentifier,        int maxLength,        String versionIdentifier,        int minLength,        int length,        String definition,        String pattern,        String businessTerm    ) {
        super(
        );
        this.dictionary = dictionary;
        this.uniqueIdentifier = uniqueIdentifier;
        this.maxLength = maxLength;
        this.versionIdentifier = versionIdentifier;
        this.minLength = minLength;
        this.length = length;
        this.definition = definition;
        this.pattern = pattern;
        this.businessTerm = businessTerm;
    }


    public String getDictionary() {
        return dictionary;
    }

    public void setDictionary(String dictionary) {
        this.dictionary = dictionary;
    }
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public int getMinlength() {
        return minLength;
    }

    public void setMinlength(int minLength) {
        this.minLength = minLength;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }

    public umm_BDT getUmm_bdt() {
        return umm_bdt;
    }

    public void setUmm_bdt(umm_BDT umm_bdt) {
        this.umm_bdt = umm_bdt;
    }

}