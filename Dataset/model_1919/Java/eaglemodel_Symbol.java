





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Symbol  {

    private String name;





    private List<eaglemodel_Pin> eaglemodel_pins;




    private List<eaglemodel_Frame> eaglemodel_frames;




    private List<eaglemodel_Circle> eaglemodel_circles;




    private List<eaglemodel_Text> eaglemodel_texts;




    private eaglemodel_Symbols eaglemodel_symbols;




    private List<eaglemodel_Wire> eaglemodel_wires;




    private List<eaglemodel_Rectangle> eaglemodel_rectangles;




    private List<eaglemodel_Dimension> eaglemodel_dimensions;




    private List<eaglemodel_Polygon> eaglemodel_polygons;


    public eaglemodel_Symbol(
        String name    ) {
        this.name = name;
        this.eaglemodel_pins = new ArrayList<>();
        this.eaglemodel_frames = new ArrayList<>();
        this.eaglemodel_circles = new ArrayList<>();
        this.eaglemodel_texts = new ArrayList<>();
        this.eaglemodel_wires = new ArrayList<>();
        this.eaglemodel_rectangles = new ArrayList<>();
        this.eaglemodel_dimensions = new ArrayList<>();
        this.eaglemodel_polygons = new ArrayList<>();
    }

    public eaglemodel_Symbol(
        String name        ArrayList<eaglemodel_Pin> eaglemodel_pins,        ArrayList<eaglemodel_Frame> eaglemodel_frames,        ArrayList<eaglemodel_Circle> eaglemodel_circles,        ArrayList<eaglemodel_Text> eaglemodel_texts,        ArrayList<eaglemodel_Wire> eaglemodel_wires,        ArrayList<eaglemodel_Rectangle> eaglemodel_rectangles,        ArrayList<eaglemodel_Dimension> eaglemodel_dimensions,        ArrayList<eaglemodel_Polygon> eaglemodel_polygons    ) {
        this.name = name;
        this.eaglemodel_pins = eaglemodel_pins;
        this.eaglemodel_frames = eaglemodel_frames;
        this.eaglemodel_circles = eaglemodel_circles;
        this.eaglemodel_texts = eaglemodel_texts;
        this.eaglemodel_wires = eaglemodel_wires;
        this.eaglemodel_rectangles = eaglemodel_rectangles;
        this.eaglemodel_dimensions = eaglemodel_dimensions;
        this.eaglemodel_polygons = eaglemodel_polygons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eaglemodel_Pin> getEaglemodel_pins() {
        return eaglemodel_pins;
    }

    public void addEaglemodel_pin(Eaglemodel_pin eaglemodel_pin) {
        this.eaglemodel_pins.add(eaglemodel_pin);
    }
    public List<eaglemodel_Frame> getEaglemodel_frames() {
        return eaglemodel_frames;
    }

    public void addEaglemodel_frame(Eaglemodel_frame eaglemodel_frame) {
        this.eaglemodel_frames.add(eaglemodel_frame);
    }
    public List<eaglemodel_Circle> getEaglemodel_circles() {
        return eaglemodel_circles;
    }

    public void addEaglemodel_circle(Eaglemodel_circle eaglemodel_circle) {
        this.eaglemodel_circles.add(eaglemodel_circle);
    }
    public List<eaglemodel_Text> getEaglemodel_texts() {
        return eaglemodel_texts;
    }

    public void addEaglemodel_text(Eaglemodel_text eaglemodel_text) {
        this.eaglemodel_texts.add(eaglemodel_text);
    }
    public eaglemodel_Symbols getEaglemodel_symbols() {
        return eaglemodel_symbols;
    }

    public void setEaglemodel_symbols(eaglemodel_Symbols eaglemodel_symbols) {
        this.eaglemodel_symbols = eaglemodel_symbols;
    }
    public List<eaglemodel_Wire> getEaglemodel_wires() {
        return eaglemodel_wires;
    }

    public void addEaglemodel_wire(Eaglemodel_wire eaglemodel_wire) {
        this.eaglemodel_wires.add(eaglemodel_wire);
    }
    public List<eaglemodel_Rectangle> getEaglemodel_rectangles() {
        return eaglemodel_rectangles;
    }

    public void addEaglemodel_rectangle(Eaglemodel_rectangle eaglemodel_rectangle) {
        this.eaglemodel_rectangles.add(eaglemodel_rectangle);
    }
    public List<eaglemodel_Dimension> getEaglemodel_dimensions() {
        return eaglemodel_dimensions;
    }

    public void addEaglemodel_dimension(Eaglemodel_dimension eaglemodel_dimension) {
        this.eaglemodel_dimensions.add(eaglemodel_dimension);
    }
    public List<eaglemodel_Polygon> getEaglemodel_polygons() {
        return eaglemodel_polygons;
    }

    public void addEaglemodel_polygon(Eaglemodel_polygon eaglemodel_polygon) {
        this.eaglemodel_polygons.add(eaglemodel_polygon);
    }

}