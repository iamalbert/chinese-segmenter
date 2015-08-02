import java.io.PrintStream;
import java.util.List;
import java.util.Properties;

import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreLabel;


/** This is a very simple demo of calling the Chinese Word Segmenter
 *  programmatically.  It assumes an input file in UTF8.
 *  <p/>
 *  <code>
 *  Usage: java -mx1g -cp seg.jar SegDemo fileName
 *  </code>
 *  This will run correctly in the distribution home directory.  To
 *  run in general, the properties for where to find dictionaries or
 *  normalizations have to be set.
 *
 *  @author Christopher Manning
 */

public class DemoSeg {
  

  private static final String basedir = System.getProperty("SegDemo", "data");

  private static CRFClassifier<CoreLabel> segmenter = null;

  public static final CRFClassifier<CoreLabel> getSegmenter() throws Exception{
    if ( segmenter == null ){
      System.setOut(new PrintStream(System.out, true, "utf-8"));
      Properties props = new Properties();
      props.setProperty("sighanCorporaDict", basedir);
      // props.setProperty("NormalizationTable", "data/norm.simp.utf8");
      // props.setProperty("normTableEncoding", "UTF-8");
      // below is needed because CTBSegDocumentIteratorFactory accesses it
      props.setProperty("serDictionary", basedir + "/dict-chris6.ser.gz");
      props.setProperty("inputEncoding", "UTF-8");
      props.setProperty("sighanPostProcessing", "true");

      segmenter = new CRFClassifier<CoreLabel>(props);
      segmenter.loadClassifierNoExceptions(basedir + "/ctb.gz", props);
    }
    return segmenter;
  }
  public static List<String> segment( String str ) throws Exception{
    return getSegmenter().segmentString(str);
  }

  public static void main(String[] args) throws Exception {
    String sample = "我住在美国。";
    System.out.println( segment(sample) );
  }
}
