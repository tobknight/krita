/* This file is part of the KDE project
   Copyright (C) 2017 Alexey Kapustin <akapust1n@mail.ru>


   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public
   License as published by the Free Software Foundation; either
   version 2 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public License
   along with this library; see the file COPYING.LIB.  If not, write to
   the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
*/

#ifndef KIS_TELEMETRY_REGULAR_PROVIDER_H
#define KIS_TELEMETRY_REGULAR_PROVIDER_H
#include "QScopedPointer"
#include <QVariant>
#include <KUserFeedback/AbstractDataSource>
#include <KUserFeedback/QtVersionSource>
#include <KUserFeedback/CompilerInfoSource>
#include <KUserFeedback/LocaleInfoSource>
#include <KUserFeedback/OpenGLInfoSource>
#include <KUserFeedback/PlatformInfoSource>
#include <KUserFeedback/QtVersionSource>
#include <KUserFeedback/ScreenInfoSource>
#include <KUserFeedback/provider.h>

#include "kis_cpuinfosource.h"

#include <kis_telemetry_abstruct.h>
#include <memory>
#include <QVector>
#include <QMultiMap>
#include <QWeakPointer>
#include "kis_tickets.h"


class KisTelemetryRegularProvider : public KisTelemetryAbstruct {
public:
    KisTelemetryRegularProvider();
    void sendData(QString path) override;
    void getTimeTicket(QString id, UseMode mode = Activate) override;
    void putTimeTicket(QString id,  UseMode mode = Activate) override;

    virtual ~KisTelemetryRegularProvider();

private:
    enum TelemetryCategory{
        tools
    };
private:
    QScopedPointer<KUserFeedback::Provider> m_toolsProvider;
    std::vector<std::unique_ptr<KUserFeedback::AbstractDataSource> > m_toolSources;
    QMultiMap<QString, QWeakPointer<KisTicket>> m_tickets;
    TelemetryCategory pathToKind(QString path);

};

#endif
