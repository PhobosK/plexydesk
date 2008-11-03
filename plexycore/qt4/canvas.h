#ifndef _CANVAS_H_
#define _CANVAS_H_

#include <QtGui>
#include <backdropinterface.h>
#include <pluginloader.h>
#include <baseplugin.h>
#include <backdropplugin.h>
#include <widgetplugin.h>
#include <frameitem.h>


/**
 * \class Canvas
 * \brief 
 */
namespace PlexyDesk
{
  
class Canvas : public QGraphicsScene
{
  Q_OBJECT
public:
  Canvas ( QObject * parent = 0 );
  ~Canvas();
protected:
  virtual void drawBackground ( QPainter * painter, const QRectF & rect );
  virtual void dropEvent( QGraphicsSceneDragDropEvent * event ); 
  virtual void dragEnterEvent(QGraphicsSceneDragDropEvent *event);
private:
    class Private;
    Private * const d;
};
  
} /* PlexyDesk */


#endif /* _CANVAS_H_ */
