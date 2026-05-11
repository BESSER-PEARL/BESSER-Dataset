





import java.util.List;
import java.util.ArrayList;

public class model_DoorsObject extends DoorsTreeNode {

    private String objectIdentifier;
    private String objectNumber;
    private String objectText;
    private String objectShortText;
    private String text;
    private String objectHeading;
    private int absoluteNumber;



    public model_DoorsObject(
        String objectIdentifier,        String objectNumber,        String objectText,        String objectShortText,        String text,        String objectHeading,        int absoluteNumber    ) {
        super(
        );
        this.objectIdentifier = objectIdentifier;
        this.objectNumber = objectNumber;
        this.objectText = objectText;
        this.objectShortText = objectShortText;
        this.text = text;
        this.objectHeading = objectHeading;
        this.absoluteNumber = absoluteNumber;
    }


    public String getObjectidentifier() {
        return objectIdentifier;
    }

    public void setObjectidentifier(String objectIdentifier) {
        this.objectIdentifier = objectIdentifier;
    }
    public String getObjectnumber() {
        return objectNumber;
    }

    public void setObjectnumber(String objectNumber) {
        this.objectNumber = objectNumber;
    }
    public String getObjecttext() {
        return objectText;
    }

    public void setObjecttext(String objectText) {
        this.objectText = objectText;
    }
    public String getObjectshorttext() {
        return objectShortText;
    }

    public void setObjectshorttext(String objectShortText) {
        this.objectShortText = objectShortText;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getObjectheading() {
        return objectHeading;
    }

    public void setObjectheading(String objectHeading) {
        this.objectHeading = objectHeading;
    }
    public int getAbsolutenumber() {
        return absoluteNumber;
    }

    public void setAbsolutenumber(int absoluteNumber) {
        this.absoluteNumber = absoluteNumber;
    }


}