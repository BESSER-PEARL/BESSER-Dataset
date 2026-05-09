





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Polygon  {

    private int layer;
    private float width;
    private int rank;
    private boolean thermals;
    private float spacing;
    private boolean orphans;
    private float isolate;
    private String pour;





    private eaglemodel_Package eaglemodel_package;




    private eaglemodel_Plain eaglemodel_plain;


    public eaglemodel_Polygon(
        int layer,        float width,        int rank,        boolean thermals,        float spacing,        boolean orphans,        float isolate,        String pour    ) {
        this.layer = layer;
        this.width = width;
        this.rank = rank;
        this.thermals = thermals;
        this.spacing = spacing;
        this.orphans = orphans;
        this.isolate = isolate;
        this.pour = pour;
    }


    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public boolean getThermals() {
        return thermals;
    }

    public void setThermals(boolean thermals) {
        this.thermals = thermals;
    }
    public float getSpacing() {
        return spacing;
    }

    public void setSpacing(float spacing) {
        this.spacing = spacing;
    }
    public boolean getOrphans() {
        return orphans;
    }

    public void setOrphans(boolean orphans) {
        this.orphans = orphans;
    }
    public float getIsolate() {
        return isolate;
    }

    public void setIsolate(float isolate) {
        this.isolate = isolate;
    }
    public String getPour() {
        return pour;
    }

    public void setPour(String pour) {
        this.pour = pour;
    }

    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }
    public eaglemodel_Plain getEaglemodel_plain() {
        return eaglemodel_plain;
    }

    public void setEaglemodel_plain(eaglemodel_Plain eaglemodel_plain) {
        this.eaglemodel_plain = eaglemodel_plain;
    }

}