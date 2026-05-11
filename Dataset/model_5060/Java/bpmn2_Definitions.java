





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String exporter;
    private String typeLanguage;
    private String targetNamespace;
    private String expressionLanguage;
    private String exporterVersion;
    private String name;



    public bpmn2_Definitions(
        String exporter,        String typeLanguage,        String targetNamespace,        String expressionLanguage,        String exporterVersion,        String name    ) {
        super(
        );
        this.exporter = exporter;
        this.typeLanguage = typeLanguage;
        this.targetNamespace = targetNamespace;
        this.expressionLanguage = expressionLanguage;
        this.exporterVersion = exporterVersion;
        this.name = name;
    }


    public String getExporter() {
        return exporter;
    }

    public void setExporter(String exporter) {
        this.exporter = exporter;
    }
    public String getTypelanguage() {
        return typeLanguage;
    }

    public void setTypelanguage(String typeLanguage) {
        this.typeLanguage = typeLanguage;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getExporterversion() {
        return exporterVersion;
    }

    public void setExporterversion(String exporterVersion) {
        this.exporterVersion = exporterVersion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}